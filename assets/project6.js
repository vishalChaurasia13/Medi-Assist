$(document).ready(function ()
{
var medicine = 1
$('#tbody').on("click","#save", function(){
   var st=""

    if($('#stod'+(medicine-1)).is(":checked"))
        st="OD"
    else if($('#stbd'+(medicine-1)).is(":checked"))
        st="BD"
    else if($('#sttid'+(medicine-1)).is(":checked"))
        st="TID"
    else if($('#sths'+(medicine-1)).is(":checked"))
        st="HS"

    alert($('#med'+(medicine-1)).val()+","+$('#textarea'+(medicine-1)).val()+","+st)
    $.getJSON("/add_prescription",{prescription:$('#med'+(medicine-1)).val(),remark:$('#textarea'+(medicine-1)).val(),timemed:st},function (data) {
        if(data.result)
        { alert("Submitted")}
        else
        {alert("Fail to Submit") }

    })

    })


$("select").material_select();


$('#add').click(function()
{
h=""
h+="<tr><td><div class='input-field col s12'><input placeholder='Medicine'"+(medicine+1)+"'type='text' id='med"+medicine+"'  ></div></td>"
h+="<td><div class='input-field col s12'><textarea id='textarea"+(medicine)+"'class='materialize-textarea' placeholder='Instructions'></textarea></div></td>"
h+="<td><p><label><input type='radio' class='filled-in' name='stod"+medicine+"' id='stod"+medicine+"' value='OD' /><span style='color:black;'>OD</span></label></p>"
h+="<p><label><input type='radio' class='filled-in' name='st"+medicine+"' id='stbd"+medicine+"'  value='BD'/><span style='color:black;'>BD</span></label></p>"
h+="<p><label><input type='radio' class='filled-in' name='st"+medicine+"' id='sttid"+medicine+"' value='TID' /><span style='color:black;'>TID</span></label></p>"
h+="<p><label><input type='radio' class='filled-in' name='st"+medicine+"' id='sths"+medicine+"' value='HS'/><span style='color:black;'>HS</span></label></p>"
h+="<button type='button' class='btn-floating btn-small waves-effect waves-light btn' id='save'  >"
h+="<i class='material-icons'>save</i></button>"

$('#tbody').append(h);
medicine++

});



});