$('#search_vlue').click(function(){
   var search_val = $('#stock_value').val();
   console.table(search_val) ;

   if(search_val != ''){
       $.ajax({
           url: 'portfolio-stock/',
           type: 'GET',
           data: {
               'search_value': search_val
           },
           dataType: 'json',
           success: function(data){
            if (data['status'] === 'NOT_FOUND'){
                console.log(data);
                console.log(data['status']);
                $('#uk-alert').html(`<div class="uk-alert-danger m-1 p-1 uk-box-shadow-small" uk-alert>Stock not found ! </div>`);
                
            } else {
                console.table(data);
                
                output = `
               <div class="uk-alert-primary m-1 p-1 uk-box-shadow-small" uk-alert>
                    <a class="uk-alert-close" uk-close></a>
                    <div class="row stock-card rounded-2 ">
                        <div class="col-4 stock-logo">
                            LOGO
                        </div>
                        <div class="col-7 p-1">
                            <h4 class="uk-text-bold uk-text-secondary">`+search_val+`<span class="p-1"><div class="p-1 border-success rounded text-success test d-inline border">test price</div></span></h4>
                            
                            <div class=" uk-flex uk-inline-clip">
                                <div class="uk-column-1-2 uk-text-success">High</div>
                                <div class="uk-column-1-2 uk-text-danger">Low</div>
                            </div>
                            <div class=" uk-flex uk-inline-clip">
                                <div class="uk-column-1-2 uk-text-success">`+data['data']['open']+`</div>
                                <div class="uk-column-1-2 uk-text-danger">`+data['data']['close']+`</div>
                            </div>
                        </div>
                    </div>
                </div>
           `;  
           
           $('#uk-alert').html(output);

           
            }

           },
   
       })
   };
})