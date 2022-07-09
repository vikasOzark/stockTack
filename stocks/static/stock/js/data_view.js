if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
  }
  const chatSocket = new WebSocket(
          'ws://'
          + window.location.host
          + '/ws/stock-price'
          + '/'
      )
      
      chatSocket.onmessage = function(e) {
          const data = JSON.parse(e.data);
          console.log(data.message);
      };

      chatSocket.onclose = function(e) {
          console.error('Chat socket closed unexpectedly');
      };