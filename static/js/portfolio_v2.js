$('#search_vlue').click(function(){
   var search_val = $('#stock_value').val();

   if(search_val != ''){
       $.ajax({
           url: 'stock-data/',
           type: 'GET',
           data: {
               'search_value': search_val
           },
           dataType: 'json',
           success: function(data){
    
            if (data['data'] == 'NOT_FOUND'){
                $('#uk-alert').html(`<div class="uk-alert-danger m-1 p-1 uk-box-shadow-small" uk-alert>Stock not found ! </div>`);

            } else {

                output = 
                  `
                    <div class="uk-alert-success" uk-alert>
                        <a class="uk-alert-close" uk-close></a>
                        <h5 class="uk-text-bold uk-text-secondary">`+search_val+`</h5>
                        <p>Price : `+data['data']['price']+`</p>
                    </div>
                  `;  
  
           $('#uk-alert').html(output);   
           $('#stock_name').val('');    
           $('#stock_name').val(search_val);    
            }

           },
   
       })
   };
})

// UIkit.notify({
//     message : 'Bazinga!',
//     status  : 'primary',
//     timeout : 5000,
//     pos     : 'top-center'
// });


var submit = document.getElementById('submit-form');
submit.addEventListener('click', function(){
    var stock_name = $('#stock_name').val();
    var stock_price = $('#stock_price').val();
    var stock_quantity = $('#stock_quantity').val();
    var stock_date = $('#stock_date').val();
    var token =  $('input[name="csrfmiddlewaretoken"]').attr('value'); 

    $.ajax({
        url: 'portfolio-stock/',
        type: 'POST',   
        data: {
            'stock_name': stock_name,
            'stock_price': stock_price,
            'stock_quantity': stock_quantity,
            'stock_date': stock_date,
            'csrfmiddlewaretoken': token ,
            },

        dataType: 'json',
        success: function(data){
            var message = data['success']; 
            var _status = data['status'];

            if(_status == 200){
                alert(message);
            };
            $('#form-stock')[0].reset();
            $('#stock_value').val('');

        }
    })
})

var upload_btn  = document.getElementById('download-btn');
upload_btn.addEventListener('click', function(){

    $.ajax({
        url : 'excel_upload/',
        type : 'GET',
        success : function(data) {
            alert('Excel file downloded successfully');
        }
    });
})

// var upload_btn  = document.getElementById('upload-btn');
// upload_btn.addEventListener('click', function(){
//     var token =  $('input[name="csrfmiddlewaretoken"]').attr('value'); 
//     var file_data = $('#file_data');
//     alert(file_data);
//     console.log(file_data);

// })