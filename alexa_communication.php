<?php
$alexa_request = file_get_contents( 'php://input');


//$empty = fopen("/home/pi/alexa_communication/alexa_response.json", "w");
//fwrite($empty, "");
//fclose($empty);

$myfile = fopen("/home/pi/alexa_communication/alexa_request.json", "w") or die("Unable to open file!");

fwrite($myfile, $alexa_request);
fclose($myfile);

sleep(2);
//while (filesize("/home/pi/alexa_communication/alexa_response.json") == 0) {
        
//}

//exec("python wait_on_response.py", $response);



$response = file_get_contents("/home/pi/alexa_communication/alexa_response.json");
//$empty = fopen("/home/pi/alexa_communication/alexa_response.json", "w+");
//fwrite($empty, "");
//fclose($empty);

echo $response;
?>