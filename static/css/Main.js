
var logflag =1;
var aboutflag =1;


function login(){
    var loginflag =  document.getElementById("log-in");
    if(logflag==0){
   
        loginflag.style.display="none";
        logflag =1;
        
    }
    else{
    
       loginflag.style.display="block";
        logflag=0;
    }

}


function aboutpage(){
    var aboutpageflag = document.getElementById("about-page");
    
    if(aboutflag==0){
        aboutpageflag.style.display="none";
        aboutflag=1;

    }
    else {
        aboutpageflag.style.display="block";
        aboutflag=0;
    }
}
function test(){
    alert('hi');
}

function oldpersonname(){
  var name = document.getElementById("oldpersonname")
  alert(name)
}