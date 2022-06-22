$('#search_vlue').click(function(){
   var search_val = $('#stock_value').val();

   if(search_val != ''){
       $.ajax({
           url: 'portfolio-stock/',
           type: 'GET',
           data: {
               'search_value': search_val
           },
           dataType: 'json',
           success: function(data){
            console.table('data', data);
            if (data['data'] == 'NOT_FOUND'){
                $('#uk-alert').html(`<div class="uk-alert-danger m-1 p-1 uk-box-shadow-small" uk-alert>Stock not found ! </div>`);

            } else {
                output = 
                  `
                  <div class="uk-alert-primary" style="width: 35rem;" uk-alert>
                    <a class="uk-alert-close" uk-close></a>
                    <div class="row stock-card rounded-2 ">
                        <div class="col-4 comp-logo">
                            LOGO
                        </div>
                        <div class="col-7 p-1">
                            <h4 class="uk-text-bold uk-text-secondary">`+search_val+`</h4>
                            <h5 class="p-1 border text-black-50 d-flex float-end" id="stock-data-get" >test price</h5>
                            
                            <div class=" uk-flex uk-inline-clip">
                                <div class="uk-column-1-2 uk-text-success">High</div>
                                <div class="uk-column-1-2 uk-text-danger">Low</div>
                            </div>
                            <div class=" uk-flex uk-inline-clip">
                                <div class="uk-column-1-2 uk-text-success" style="height:24px; width: 97px;">`+data['data']['results'][0]['h']+`</div>
                                <div class="uk-column-1-2 uk-text-danger" style="height:24px; width: 97px;">`+data['data']['results'][0]['l']+`</div>
                            </div>
                        </div>
                    </div>
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

var submit = document.getElementById('submit-form');
submit.addEventListener('click', function(){
    
})