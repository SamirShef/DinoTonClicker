mergeInto(LibraryManager.library, 
{
  SetString: function (path, objName, successCallback, errorCallback) 
  {
    var str = UTF8ToString(path);
    var passedObjName = UTF8ToString(objName);
    var onSuccess = UTF8ToString(successCallback);
    var onError = UTF8ToString(errorCallback);

    firebase.database().ref('test').set(str)
      .then(function() 
      {
        console.log('String sent to Firebase successfully.');
        unityInstance.SendMessage(passedObjName, onSuccess);
      })
      .catch(function(error) 
      {
        console.error('Error sending string to Firebase:', error);
        unityInstance.SendMessage(passedObjName, onError, error.message);
      });
  }
});