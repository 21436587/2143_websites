var theyclicked=1;
/*
function doFunction(id){
	console.log("they pressed");
	console.log(id);
	if(theyclicked%2==1){
		document.getElementById(id).value = "switch on";
	} else {
		document.getElementById(id).value = "switch off";
		}
}
*/
function setOn(id){
	theyclicked++;
	document.getElementById(id).value = "switch on";
}
function setOff(id){
	document.getElementById(id).value = "switch off";
}
function getVal(id){
	return document.getElementById(id).value;
}
function setThis(id, st, dis=true){
	document.getElementById(id).value = st;
	document.getElementById(id).disabled = dis;
}
function resetValue(id){
	console.log("resetting the values");
	document.getElementById(id).value = "click to the button to reveal results";
}
/*
function isThisReal(){
	    alert(document.getElementById('clickMe').value)
	}
*/