(() => {
"use strict";

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
const W = canvas.width, H = canvas.height;
const keys = Object.create(null);
const mouse = {x: W/2, y: H/2, down:false};

window.addEventListener("keydown", e => {
  const k=e.key.toLowerCase();
  keys[k]=true;
  if(k==="r") resetGame();
  if(k==="p") paused=!paused;
  if(state==="select" && ["1","2","3","4"].includes(k)) chooseCharacter(+k-1);
});
window.addEventListener("keyup", e => keys[e.key.toLowerCase()]=false);
canvas.addEventListener("mousemove", e=>{
  const r=canvas.getBoundingClientRect();
  mouse.x=(e.clientX-r.left)*W/r.width;
  mouse.y=(e.clientY-r.top)*H/r.height;
});
canvas.addEventListener("mousedown",()=>mouse.down=true);
window.addEventListener("mouseup",()=>mouse.down=false);

const TAU=Math.PI*2;
const rand=(a,b)=>a+Math.random()*(b-a);
const randi=(a,b)=>Math.floor(rand(a,b+1));
const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
const pick=a=>a[Math.floor(Math.random()*a.length)];
const distance=(a,b)=>Math.hypot(a.x-b.x,a.y-b.y);

function text(s,x,y,size=16,color="#fff",align="left"){
  ctx.font=`${size}px Arial`;
  ctx.fillStyle=color;
  ctx.textAlign=align;
  ctx.fillText(s,x,y);
  ctx.textAlign="left";
}
function circle(x,y,r,color){
  ctx.fillStyle=color;ctx.beginPath();ctx.arc(x,y,r,0,TAU);ctx.fill();
}
function rect(x,y,w,h,color){ctx.fillStyle=color;ctx.fillRect(x,y,w,h)}

const characters=[
  {name:"ARI",desc:"Equilibrado",color:"#e0e1e8",hp:6,speed:3.7,damage:1,fire:10,shot:8.5,start:"Lágrima Solar"},
  {name:"MIRA",desc:"Rápida e precisa",color:"#82d7e9",hp:4,speed:4.5,damage:.9,fire:7,shot:9.5,start:"Botas de Eco"},
  {name:"BRUTUS",desc:"Muito dano e vida",color:"#e0a16b",hp:8,speed:3,damage:1.35,fire:13,shot:7.5,start:"Coração de Ferro"},
  {name:"NYX",desc:"Pouca vida, tiros triplos",color:"#b18de5",hp:3,speed:4,damage:.85,fire:9,shot:8.5,start:"Olho Triplo"}
];

const items=[
  {name:"Lágrima Solar",desc:"+35% dano",apply:p=>p.damage*=1.35},
  {name:"Botas de Eco",desc:"+20% velocidade",apply:p=>p.speed*=1.20},
  {name:"Olho Triplo",desc:"Dispara 3 projéteis",apply:p=>p.multishot=Math.max(3,p.multishot)},
  {name:"Coração de Ferro",desc:"+2 vida máxima",apply:p=>{p.maxHp+=2;p.hp+=2}},
  {name:"Relógio Quebrado",desc:"+35% cadência",apply:p=>p.fire*=.65},
  {name:"Lágrima Gigante",desc:"Projéteis maiores e +20% dano",apply:p=>{p.bulletR+=3;p.damage*=1.2}},
  {name:"Sangue Frio",desc:"20% chance de crítico",apply:p=>p.crit=Math.min(.75,p.crit+.2)},
  {name:"Ímã",desc:"Atrai moedas e pickups",apply:p=>p.magnet+=80},
  {name:"Espelho",desc:"+1 vida e +10% dano",apply:p=>{p.hp=Math.min(p.maxHp,p.hp+1);p.damage*=1.1}},
  {name:"Anjo de Papel",desc:"+2 escudos",apply:p=>p.shield+=2},
  {name:"Coroa do Caos",desc:"+50% dano, -10% velocidade",apply:p=>{p.damage*=1.5;p.speed*=.9}},
  {name:"Olho de Vidro",desc:"+25% alcance e +25% projétil",apply:p=>{p.shot*=1.25;p.bulletR+=1}},
  {name:"Coração Vampiro",desc:"20% chance de curar ao matar",apply:p=>p.vamp=.2},
  {name:"Agulha",desc:"+25% velocidade e +15% crítico",apply:p=>{p.speed*=1.25;p.crit+=.15}},
  {name:"Lágrima Gélida",desc:"Projéteis lentificam inimigos",apply:p=>p.slow=.35}
];

const enemyDefs={
 crawler:{hp:3,speed:1.25,r:17,color:"#79506d"},
 bat:{hp:2,speed:2.05,r:14,color:"#685f8d"},
 shooter:{hp:4,speed:.75,r:18,color:"#8a526f",shoot:85},
 charger:{hp:5,speed:1.05,r:20,color:"#896748"},
 turret:{hp:6,speed:0,r:19,color:"#566a7c",shoot:60},
 leaper:{hp:6,speed:1.0,r:21,color:"#7a6b45"}
};

const bosses=[
 {name:"MÃE DAS SOMBRAS",hp:90,r:50,color:"#71304c",kind:"mother"},
 {name:"REI DO VAZIO",hp:125,r:57,color:"#385077",kind:"void"},
 {name:"DEUS DAS LÁGRIMAS",hp:175,r:64,color:"#87692b",kind:"god"}
];

let player=null,enemies=[],bullets=[],enemyBullets=[],pickups=[],particles=[];
let rooms=[],floor=1,roomIndex=0,score=0,coins=0,state="select",paused=false;
let shake=0,message="",messageTimer=0,selectedCharacter=0,roomSeed=0;

function resetGame(){
  state="select";paused=false;selectedCharacter=0;player=null;
  enemies=[];bullets=[];enemyBullets=[];pickups=[];particles=[];
  rooms=[];floor=1;roomIndex=0;score=0;coins=0;shake=0;
  message="";messageTimer=0;roomSeed=0;
}

function chooseCharacter(i){
  selectedCharacter=i;
  if(state==="select") startRun(i);
}

function startRun(i){
  const c=characters[i];
  player={
    x:W/2,y:H/2,r:17,
    hp:c.hp,maxHp:c.hp,speed:c.speed,damage:c.damage,fire:c.fire,shot:c.shot,
    bulletR:5,multishot:1,crit:0,magnet:0,shield:0,vamp:0,slow:0,
    inv:0,fireTimer:0,items:[],color:c.color,name:c.name
  };
  state="play";floor=1;score=0;coins=0;roomIndex=0;
  giveItem(c.start,true);
  buildFloor();
}

function buildFloor(){
  rooms=[];
  for(let i=0;i<8;i++){
    let type;
    if(i===0) type="start";
    else if(i===7) type="boss";
    else {
      const r=Math.random();
      type=r<.17?"shop":r<.37?"item":r<.44?"treasure":"combat";
    }
    rooms.push({type,cleared:false});
  }
  loadRoom(0);
}

function loadRoom(i){
  roomIndex=i;
  enemies=[];bullets=[];enemyBullets=[];pickups=[];particles=[];
  roomSeed=Math.random();
  player.x=W/2;player.y=H/2;player.inv=35;

  const room=rooms[i];
  if(room.type==="start"){room.cleared=true;return}
  if(room.type==="item"){
    room.cleared=true;
    pickups.push({type:"item",x:W/2,y:H/2,r:22,item:pick(items)});
    return;
  }
  if(room.type==="shop"){
    room.cleared=true;
    pickups.push({type:"shopItem",x:W/2-100,y:H/2,r:22,item:pick(items),price:2});
    pickups.push({type:"heart",x:W/2+100,y:H/2,r:12});
    return;
  }
  if(room.type==="treasure"){
    room.cleared=true;
    pickups.push({type:"treasure",x:W/2,y:H/2,r:24,item:pick(items)});
    return;
  }
  if(room.type==="boss"){spawnBoss();return}

  const count=4+floor+Math.floor(i*.75);
  for(let n=0;n<count;n++) spawnEnemy();
}

function spawnEnemy(forced){
  const keys=["crawler","bat","shooter","charger","turret","leaper"];
  const type=forced||pick(keys), d=enemyDefs[type];
  let x,y;
  do{x=rand(70,W-70);y=rand(115,H-55)}while(Math.hypot(x-W/2,y-H/2)<160);
  const scale=1+(floor-1)*.22;
  enemies.push({
    type,x,y,r:d.r,hp:d.hp*scale,maxHp:d.hp*scale,
    speed:d.speed,color:d.color,shoot:d.shoot||0,cd:rand(20,80),
    dash:0,jump:0,slowTimer:0
  });
}

function spawnBoss(){
  const b=bosses[Math.min(bosses.length-1,Math.floor((floor-1)/1))];
  const hp=b.hp+(floor-1)*15;
  enemies.push({boss:true,type:b.kind,name:b.name,x:W/2,y:335,r:b.r,hp,maxHp:hp,
    speed:1.05,shoot:50,cd:45,phase:0,color:b.color,spawnTimer:0});
}

function giveItem(name,silent=false){
  const it=items.find(x=>x.name===name)||items.find(x=>x.name===name.trim());
  if(!it)return;
  it.apply(player);player.items.push(it.name);
  if(!silent){
    score+=300;message=`${it.name}: ${it.desc}`;messageTimer=150;
    burst(player.x,player.y,"#e9cb69",30);
  }
}

function fire(){
  if(player.fireTimer>0)return;
  const base=Math.atan2(mouse.y-player.y,mouse.x-player.x);
  let offsets;
  if(player.multishot<=1) offsets=[0];
  else if(player.multishot===3) offsets=[-.18,0,.18];
  else offsets=[-.28,-.14,0,.14,.28];

  for(const off of offsets){
    const a=base+off;
    bullets.push({
      x:player.x+Math.cos(a)*23,y:player.y+Math.sin(a)*23,
      vx:Math.cos(a)*player.shot,vy:Math.sin(a)*player.shot,
      r:player.bulletR,life:100,dmg:player.damage
    });
  }
  player.fireTimer=player.fire;
}

function enemyFire(e,mode="aim"){
  if(mode==="ring"){
    const count=e.phase>.75?24:16;
    for(let i=0;i<count;i++){
      const a=i*TAU/count;
      enemyBullets.push({x:e.x,y:e.y,vx:Math.cos(a)*2.6,vy:Math.sin(a)*2.6,r:6,life:190,dmg:1});
    }
    return;
  }
  if(mode==="spiral"){
    for(let i=0;i<10;i++){
      const a=(i*TAU/10)+performance.now()/1000;
      enemyBullets.push({x:e.x,y:e.y,vx:Math.cos(a)*2.4,vy:Math.sin(a)*2.4,r:5,life:210,dmg:1});
    }
    return;
  }
  const a=Math.atan2(player.y-e.y,player.x-e.x);
  const n=e.boss?5:1;
  for(let i=0;i<n;i++){
    const off=n===1?0:(i-(n-1)/2)*.15;
    const ang=a+off;
    enemyBullets.push({x:e.x,y:e.y,vx:Math.cos(ang)*3.2,vy:Math.sin(ang)*3.2,r:e.boss?6:5,life:200,dmg:1});
  }
}

function burst(x,y,color,n=10){
  for(let i=0;i<n;i++){
    const a=rand(0,TAU),s=rand(1,4);
    particles.push({x,y,vx:Math.cos(a)*s,vy:Math.sin(a)*s,life:randi(18,48),color});
  }
}

function hurt(amount=1){
  if(player.inv>0)return;
  if(player.shield>0){
    player.shield--;player.inv=35;shake=4;
    burst(player.x,player.y,"#bfe8ff",15);return;
  }
  player.hp-=amount;player.inv=50;shake=9;
  burst(player.x,player.y,"#ef6979",15);
  if(player.hp<=0)state="dead";
}

function killEnemy(e){
  score+=e.boss?2500:100;
  burst(e.x,e.y,e.color,25);
  if(player.vamp>0 && Math.random()<player.vamp)
    player.hp=Math.min(player.maxHp,player.hp+1);
  if(!e.boss && Math.random()<.18)
    pickups.push({type:"heart",x:e.x,y:e.y,r:10});
  if(!e.boss && Math.random()<.08)
    pickups.push({type:"coin",x:e.x+rand(-8,8),y:e.y+rand(-8,8),r:9});
}

function clearRoom(){
  const room=rooms[roomIndex];
  if(room.cleared)return;
  room.cleared=true;
  if(room.type==="combat" && Math.random()<.65)
    pickups.push({type:"coin",x:W/2,y:H/2,r:9});
  if(room.type==="boss") nextFloor();
}

function nextFloor(){
  if(floor>=3){state="win";return}
  floor++;
  message=`ANDAR ${floor}`;messageTimer=120;
  buildFloor();
}

function update(){
  if(paused||state!=="play")return;
  if(player.inv>0)player.inv--;
  if(player.fireTimer>0)player.fireTimer--;
  if(shake>0)shake*=.84;
  if(messageTimer>0)messageTimer--;

  let dx=(keys.d||keys.arrowright?1:0)-(keys.a||keys.arrowleft?1:0);
  let dy=(keys.s||keys.arrowdown?1:0)-(keys.w||keys.arrowup?1:0);
  const len=Math.hypot(dx,dy)||1;
  player.x+=dx/len*player.speed;player.y+=dy/len*player.speed;
  player.x=clamp(player.x,38,W-38);player.y=clamp(player.y,98,H-38);

  if(mouse.down)fire();

  const room=rooms[roomIndex];
  // saída superior
  if(room.cleared && roomIndex<7 && player.y<110 && Math.abs(player.x-W/2)<65){
    loadRoom(roomIndex+1);return;
  }

  // pickups
  for(let i=pickups.length-1;i>=0;i--){
    const p=pickups[i],dd=distance(player,p);
    if(player.magnet>0 && dd<player.magnet){
      const pull=p.type==="coin"||p.type==="heart"||p.type==="item"||p.type==="shopItem"||p.type==="treasure";
      if(pull && dd>1){p.x+=(player.x-p.x)/dd*2.4;p.y+=(player.y-p.y)/dd*2.4;}
    }
    if(dd<player.r+p.r+7){
      if(p.type==="heart"){
        if(player.hp<player.maxHp){player.hp++;pickups.splice(i,1);}
      }else if(p.type==="coin"){
        coins++;score+=50;pickups.splice(i,1);
      }else if(p.type==="item"){
        giveItem(p.item.name);pickups.splice(i,1);
      }else if(p.type==="treasure"){
        giveItem(p.item.name);pickups.splice(i,1);
      }else if(p.type==="shopItem"){
        if(coins>=p.price){coins-=p.price;giveItem(p.item.name);pickups.splice(i,1);}
      }
    }
  }

  // tiros
  for(const b of bullets){
    b.x+=b.vx;b.y+=b.vy;b.life--;
    for(const e of enemies){
      if(e.hp<=0)continue;
      if(Math.hypot(b.x-e.x,b.y-e.y)<b.r+e.r){
        const crit=Math.random()<player.crit;
        const damage=b.dmg*(crit?2:1);
        e.hp-=damage;
        if(player.slow>0){e.slowTimer=60;}
        b.life=0;burst(b.x,b.y,crit?"#fff1a3":"#f0dfa0",crit?7:4);
        if(e.hp<=0)killEnemy(e);
        break;
      }
    }
  }
  bullets=bullets.filter(b=>b.life>0&&b.x>-40&&b.x<W+40&&b.y>65&&b.y<H+40);

  // inimigos
  for(const e of enemies){
    if(e.hp<=0)continue;
    const a=Math.atan2(player.y-e.y,player.x-e.x);
    const dd=distance(e,player);
    const slow=e.slowTimer>0?.55:1;
    if(e.slowTimer>0)e.slowTimer--;

    if(e.boss){
      e.phase=1-e.hp/e.maxHp;
      const speed=e.speed*(e.phase>.5?1.25:1)*slow;
      e.x+=Math.cos(a)*speed*(dd>230?1:.25);
      e.y+=Math.sin(a)*speed*(dd>230?1:.25);
      e.cd--;
      if(e.cd<=0){
        if(e.type==="mother"){
          if(e.phase>.45&&Math.random()<.45)enemyFire(e,"ring");else enemyFire(e);
        }else if(e.type==="void"){
          if(e.phase>.55&&Math.random()<.5)enemyFire(e,"spiral");else enemyFire(e);
        }else{
          if(e.phase>.65)enemyFire(e,"ring");else enemyFire(e);
        }
        e.cd=e.phase>.65?28:e.phase>.35?42:58;
        if(Math.random()<.22&&e.phase>.25){
          spawnEnemy(pick(["bat","crawler","shooter"]));
        }
      }
    }else{
      if(e.type==="charger"&&e.dash<=0&&Math.random()<.008)e.dash=28;
      if(e.type==="leaper"&&e.jump<=0&&Math.random()<.01)e.jump=35;
      if(e.dash>0){e.x+=Math.cos(a)*5;e.y+=Math.sin(a)*5;e.dash--}
      else if(e.jump>0){e.x+=Math.cos(a)*2.7;e.y+=Math.sin(a)*2.7;e.jump--}
      else if(e.speed>0){e.x+=Math.cos(a)*e.speed*slow;e.y+=Math.sin(a)*e.speed*slow}
      e.cd--;
      if(e.shoot&&e.cd<=0){enemyFire(e);e.cd=e.shoot*rand(.75,1.25)}
    }
    e.x=clamp(e.x,e.r,W-e.r);e.y=clamp(e.y,91+e.r,H-e.r);
    if(dd<e.r+player.r)hurt(1);
  }

  // tiros inimigos
  for(const b of enemyBullets){
    b.x+=b.vx;b.y+=b.vy;b.life--;
    if(Math.hypot(b.x-player.x,b.y-player.y)<b.r+player.r){
      b.life=0;hurt(b.dmg);
    }
  }
  enemyBullets=enemyBullets.filter(b=>b.life>0&&b.x>-50&&b.x<W+50&&b.y>65&&b.y<H+50);

  for(const p of particles){
    p.x+=p.vx;p.y+=p.vy;p.vx*=.95;p.vy*=.95;p.life--;
  }
  particles=particles.filter(p=>p.life>0);

  if(enemies.length && enemies.every(e=>e.hp<=0))clearRoom();
}

function drawFloor(){
  rect(0,0,W,H,"#08090d");
  const boss=rooms[roomIndex]?.type==="boss";
  rect(30,80,W-60,H-105,boss?"#17131b":"#171923");
  ctx.strokeStyle="#3a3d4a";ctx.lineWidth=10;ctx.strokeRect(30,80,W-60,H-105);
  ctx.strokeStyle="#222530";ctx.lineWidth=1;
  for(let x=50;x<W-40;x+=40){ctx.beginPath();ctx.moveTo(x,85);ctx.lineTo(x,H-30);ctx.stroke();}
  for(let y=100;y<H-35;y+=40){ctx.beginPath();ctx.moveTo(35,y);ctx.lineTo(W-35,y);ctx.stroke();}
  for(let i=0;i<22;i++){
    const x=55+(i*173)%1000,y=105+(i*97)%540;
    rect(x,y,7,4,"#11131b");
  }
}

function draw(){
  ctx.save();
  const sx=shake?(Math.random()-.5)*shake:0,sy=shake?(Math.random()-.5)*shake:0;
  ctx.translate(sx,sy);
  drawFloor();

  const room=rooms[roomIndex],cleared=room?.cleared;
  if(cleared&&roomIndex<7){
    rect(W/2-48,72,96,18,"#d9bc68");
    text("SAÍDA",W/2,112,12,"#d9bc68","center");
  }

  for(const p of pickups){
    if(p.type==="item"||p.type==="treasure"||p.type==="shopItem"){
      circle(p.x,p.y,25,p.type==="shopItem"?"#87653b":"#b38a45");
      circle(p.x,p.y,19,"#e4cf78");
      text(p.type==="treasure"?"★":p.type==="shopItem"?p.price+"¢":"?",p.x,p.y+8,20,"#4b381e","center");
    }else if(p.type==="coin"){
      circle(p.x,p.y,10,"#e6c65e");circle(p.x,p.y,5,"#fff1a0");
    }else{
      circle(p.x,p.y,11,"#d75c6d");text("+",p.x,p.y+6,16,"#fff","center");
    }
  }

  for(const e of enemies)if(e.hp>0){
    circle(e.x,e.y,e.r,e.color);
    if(e.boss){
      ctx.strokeStyle="#e6c96c";ctx.lineWidth=3;ctx.strokeRect(e.x-e.r-5,e.y-e.r-5,e.r*2+10,e.r*2+10);
    }
    circle(e.x-6,e.y-4,4,"#f1b0ba");circle(e.x+6,e.y-4,4,"#f1b0ba");
    rect(e.x-e.r,e.y-e.r-11,e.r*2,5,"#07080c");
    rect(e.x-e.r,e.y-e.r-11,e.r*2*(e.hp/e.maxHp),5,"#d35c6d");
  }

  for(const b of bullets)circle(b.x,b.y,b.r,"#f1dfa0");
  for(const b of enemyBullets)circle(b.x,b.y,b.r,"#d86d9a");

  if(player && player.inv%6<3){
    circle(player.x,player.y,player.r,player.color);
    if(player.shield>0){
      ctx.strokeStyle="#bfe7ff";ctx.lineWidth=3;ctx.beginPath();ctx.arc(player.x,player.y,player.r+8,0,TAU);ctx.stroke();
    }
    const a=Math.atan2(mouse.y-player.y,mouse.x-player.x);
    ctx.strokeStyle="#fff";ctx.lineWidth=5;ctx.beginPath();
    ctx.moveTo(player.x,player.y);ctx.lineTo(player.x+Math.cos(a)*28,player.y+Math.sin(a)*28);ctx.stroke();
  }

  for(const p of particles){
    ctx.globalAlpha=Math.max(0,p.life/45);circle(p.x,p.y,3,p.color);ctx.globalAlpha=1;
  }
  ctx.restore();

  // HUD
  rect(0,0,W,72,"#08090ddd");
  text("DUNGEON TEARS",18,27,21,"#eee5cf");
  text(`Andar ${floor}  •  Sala ${roomIndex+1}/8`,18,51,14,"#b9beca");
  text(`Moedas ${coins}  •  Pontos ${score}`,190,51,14,"#b9beca");
  if(player){
    text("♥".repeat(Math.max(0,player.hp)),18,68,18,"#e66c78");
    text("♥".repeat(Math.max(0,player.maxHp-player.hp)),18+player.maxHp*15,68,18,"#4b4e58");
    text(player.items.length?player.items.join("  •  "):"Sem itens",W/2,51,12,"#a8adba","center");
  }
  if(room?.type==="boss"&&enemies[0]?.hp>0){
    text(enemies[0].name,W/2,94,18,"#e4c875","center");
  }
  if(messageTimer>0)text(message,W/2,H-20,17,"#f0d47a","center");

  if(state==="select")drawSelect();
  if(state==="dead")overlay("VOCÊ MORREU","#e16c79","Pressione R para reiniciar");
  if(state==="win")overlay("VOCÊ VENCEU!","#e6cd70","Pressione R para jogar novamente");
  if(paused&&state==="play")overlay("PAUSADO","#d9dce5","Pressione P para continuar");
}

function drawSelect(){
  rect(0,0,W,H,"#04050be8");
  text("DUNGEON TEARS DELUXE",W/2,115,48,"#ead8a5","center");
  text("Escolha seu personagem — teclas 1, 2, 3 ou 4",W/2,151,19,"#c2c6d1","center");
  characters.forEach((c,i)=>{
    const x=145+i*287,y=280,selected=i===selectedCharacter;
    rect(x-120,y-80,240,260,selected?"#292c3a":"#171923");
    ctx.strokeStyle=selected?"#e2c86c":"#3a3d4a";ctx.lineWidth=3;ctx.strokeRect(x-120,y-80,240,260);
    circle(x,y,34,c.color);
    text(c.name,x,y+78,22,"#eee","center");
    text(c.desc,x,y+105,14,"#abb0bc","center");
    text(`Vida ${c.hp} • Dano ${c.damage}`,x,y+130,13,"#c7cad2","center");
    text(`Começa com: ${c.start}`,x,y+151,12,"#9da3b1","center");
    text(String(i+1),x,y+183,16,"#e2c86c","center");
  });
}

function overlay(title,color,sub){
  rect(0,0,W,H,"#04050be0");
  text(title,W/2,H/2-25,56,color,"center");
  text(sub,W/2,H/2+22,20,"#d1d4dc","center");
}

function loop(){update();draw();requestAnimationFrame(loop);}
resetGame();
loop();
})();