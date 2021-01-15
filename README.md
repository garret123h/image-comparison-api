# Image comparison API

## Instructions
Open terminal and navigate to directory.<br />
Next type in: 'python3 app.py username password' and replace 'username' with desired username and 'password' with desired password.<br />
Next open another tab in the terminal and enter in some curl commands. In the sample_curl.txt there are sample curl texts to use such as:<br />

curl -u admin http://127.0.0.1:5000/comp/fake-id/ \<br />
  --header "Content-Type: application/json" \<br />
  --request GET\<br />
  --data '{"image-one":"./sample_images/original_golden_bridge.jpg",<br />
            "image-two":"./sample_images/old_photo.jpg"<br />
            }' <br />
            
 or<br />
 
 curl -u admin http://127.0.0.1:5000/comp/fake-id/ \<br />
  --header "Content-Type: application/json" \<br />
  --request GET\<br />
  --data '{"image-one":"https://github.com/garret123h/image-comparison-api/blob/main/sample_images/original_golden_bridge.jpg?raw=true",<br />
            "image-two":"https://github.com/garret123h/image-comparison-api/blob/main/sample_images/old_photo.jpg?raw=true"<br />
            }' <br />


Note: where the '-u admin' is, replace admin with your username.<br />
Add desired images either by relative path, absolute path, or URL.<br />

The program does not take into consideration images that are different sizes. So only input same sized images.<br />

Sample testing images:<br />
![alt text](https://github.com/garret123h/image-comparison-api/blob/main/run_program.png?raw=true)
![alt text](https://github.com/garret123h/image-comparison-api/blob/main/curl_one.png?raw=true)
![alt text](https://github.com/garret123h/image-comparison-api/blob/main/curl_two.png?raw=true)
