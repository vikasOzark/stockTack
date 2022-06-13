$('#search_vlue').click(function(){
   var search_val = $('#stock_value').val();
   console.table(search_val) ;

   $.ajax({
        url: 'portfolio-stock/',
        type: 'GET',
        data: {
            'search_val': search_val
        },
        dataType: 'json',
        success: function(data){
            console.table(data)
        }    

   })
})