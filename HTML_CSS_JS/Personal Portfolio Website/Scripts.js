function animateLogo (logoname){
    if (logoname==="education"){
        document.getElementById("education").setAttribute(src, "/Images/Education2");

    }
    if (logoname==="experience"){
         document.getElementById("Experience").setAttribute(src, "/Images/Experience2");
    }
    else{
         document.getElementById("summary").setAttribute(src, "/Images/Summary2");
    }
    

}