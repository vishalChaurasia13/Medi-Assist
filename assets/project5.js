  $(document).ready(function(){
    $('.modal').modal();
    $('.collapsible').collapsible();
    var ques = []
    var subques = []
    var subqlist = {}
    var h = ""

  $('.btnshow').click(function()
  {


    docspl = $(this).attr('docspl')
    name = $(this).attr('username')
    number = $(this).attr('usernum')
    date = $(this).attr('date')
    time = $(this).attr('time')
    userdoctorid = $(this).attr('userdoctorid')



    $.getJSON('/getuserscore',{'userdoctorid':userdoctorid, 'docspl': docspl},function(data)
    { alert(JSON.stringify(data.result))
    score = data.result
    questions = data.questions



    for(i=0;i<questions.length;i++)
    {
    ques.push(questions[i]['question'])
    subques.push(questions[i]['subquestions'])
    }

    for(k=0;k<subques.length;k++)
    {
    subqlist['subque'+(k+1)] = subques[k].split('#')
    }

    for(l=0;l<ques.length;l++)
    {
        h+="<tr><td>"+(l+1)+".<td>"+ques[l]+"</td><td>"+subqlist['subque'+(l+1)]+"</td><td>"+score[l]['totalscore']+"/"+subqlist['subque'+(l+1)].length*5+"</td></tr>"
    }


    $('#tbody').html(h)


    })

    // fixing the inner html of details
    $('#name').html("<b>Name: "+name+"</b>")
    $('#mobile').html("<b>Mobile: "+number+"</b>")
    $('#Date').html("<b>Date: "+date+"</b>")
    $('#time').html("<b>Time: "+time+"</b>")

    // fixinng values for hidden inputs

    $('#username').val(name)
    $('#usermob').val(number)
    $('#userdate').val(date)
    $('#usertime').val(time)




    // getting questions and score of patient



  var modal1open = M.Modal.getinstance($('#modal1'))
  modal1open.open();





  })

  });
     