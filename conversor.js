






function GrausPf(){
    gF = GpF.value
    GRAUSF=(gF*9/5)+32
   RGpF.innerHTML = GRAUSF
}
 function GrausPk(){
  gK = parseInt (GpK.value)
  GRAUSK=(gK+273)
  RGpK.innerHTML= GRAUSK
 }
 function fahrenheitPg(){
  Fg = FpG.value
  FARG = (Fg-32)*5/9
  FHpG.innerHTML= FARG
 }