Key Lessons
JSON vs HTML
You could have the server return JSON or HTML
Return JSON if you want other developers to use the data and format the data however they want
Return HTML if you are going to use the data within your own app and you want it formatted certain way.  It's much easier to put together html using templates than use Javascript to convert JSON data to HTML (plus it's really the template's job to put together html and not necessarily Javascript).
Ajax Form
It's always better to put all the key information you need to send to the server in a form
This will make your Ajax request much easier as you can send all the information in the form by using serialize()
Example: Google Maps, Ajax Pagination, etc.
Ajax Debugging
Use Inspect Element heavily.  Console.log and also refer to the Network Tab to help you visualize.
Others
Ajax although simple in concept, could be quite difficult as it's often much harder to debug.  Don't give up though!
You will later use how to use frameworks like Angular, ReactJS, and others to do Ajax requests.
JavaScript / jQuery Debugging Steps (Use Google Chrome, Please)
1. INSPECT ELEMENT
The very first thing that you should do when debugging javascript is to inspect the element and look at the console tab to see if there are any errors in your JavaScript code. The JavaScript console may tell you where in your JavaScript code there are syntax errors, saving you lots and lots of time in debugging.

2. Use alert() or console.log()
If you don't see any error messages in the console use the alert() or console.log() functions at each line of your code to find out where the error exists. We recommend using them in the following locations in your code:

Right after the document.ready() function just to make sure your jQuery is loading properly.
Right after the .submit() handler for your form to make sure your event listener is working
Within the success function of your $.post() or $.get() function.
If you are creating variables within your jQuery or JavaScript, you can use console.log() to display the properties of them; perhaps there is an error with a particular property of an object, or you are using a string instead of a float. Stuff like that is perfect for logging to the console.

3. Check Network tab
There is a tab called 'network' when you open 'inspect element' in your browser. If you recall, this tab allows you to monitor the HTTP requests and responses sent by your web page. Check to see if your page is connecting to the file you are submitting your form to and make sure there aren't any errors on that page. Click on the tab response/preview and check whether the URL is returning data for you. If your Javascript/jQuery is working correctly, but your Python code is awry, using the network tab will allow you to see your Python errors in the response/preview tab without turning Ajax off, which is nice because that lessens the scope of potential errors!

4. Check if response is a valid json format
Force your form to submit to the page you are posting data to and make sure that the output is in valid json format. If it is not, then the problem is not with your javascript code. This can be checked by using the network tab mentioned above. The only thing that should print to the screen is the json-encoded data. This means any Python errors will make your response an invalid json format.

