$('#search_vlue').click(function(){
   var search_val = $('#stock_value').val();
   console.table(search_val) ;

   if(search_val === ''){
   		alert('Please enter the stock value');
   		return false;
   };
    $.ajax({
        url: 'portfolio-stock/',
        type: 'GET',
        data: {
            'search_value': search_val
        },
        dataType: 'json',
        success: function(data){
            console.table(data)
        }    

})
})