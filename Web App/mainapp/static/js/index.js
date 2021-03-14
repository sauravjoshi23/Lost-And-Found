// Form AJAX
$('#form').on('submit', function(e){
  e.preventDefault();

  var url = window.location.href.replace(/\/$/, '');
  var lastSeg = url.substr(url.lastIndexOf('/') + 1);

  var final_url = "/filtered_items/"+lastSeg+'/'

  $.ajax({
       type : "POST",
       url: final_url,
       data: {
        description : $('#description').val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        dataType: "json",
       },

       success: function(data){
            alert('Success')
            console.log(data)

            buildTable(data)
            //$("#output1").html(html);
//          var target = $("#output1");
//            target.empty();
//            for (var i = 0; i < data.length; i++) {
//                var item = data[i];
//                target.append("<tr><td>" + item.category_name + " </td><td> "
//                    + item.item_name + "</td></tr>");
//            }
       },
       error: function(errorMessage) {
            console.log(errorMessage)
       }
   });
});

function buildTable(data){

    var table = document.getElementById('output1')

    for (var i = 0; i < data.length; i++){
        var row = `<tr>
                        <td>${data[i].category_name}</td>
                        <td>${data[i].item_name}</td>
                        <td>${data[i].item_description}</td>
                        <td>${data[i].founder_name}</td>
                        <td>${data[i].founder_number}</td>
                  </tr>`
        table.innerHTML += row


    }
}