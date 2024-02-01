$(document).ready(function(){
var ques=[]
var i=0
$.getJSON('/helpuserquestion',{splid:6}, function(data){
//alert(JSON.stringify(data))
  ques=data.result
  htm="Q"+ques[i].questionnumber+":"+ques[i].question
  $('#questiondiv').html(htm)

})
$('#btnnext').click(function(){
    i++
    if(i<ques.length) {
        htm = "Q" + ques[i].questionnumber + ":" + ques[i].question
        $('#questiondiv').html(htm)
    }


})


})