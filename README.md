# Image comparison API


##Run API locally
Open terminal and navigate to directory.
Next type in: 'python3 app.py username password' and replace 'username' with desired username and 'password' with desired password.
Next open another tab in the terminal and enter in some curl commands. In the sample_curl.txt there are sample curl texts to use such as:

curl -u admin http://127.0.0.1:5000/comp/fake-id/ \
  --header "Content-Type: application/json" \
  --request GET\
  --data '{"image-one":"./sample_images/original_golden_bridge.jpg",
            "image-two":"./sample_images/old_photo.jpg"
            }' 
            
 or
 
 curl -u admin http://127.0.0.1:5000/comp/fake-id/ \
  --header "Content-Type: application/json" \
  --request GET\
  --data '{"image-one":"https://github.com/garret123h/image-comparison-api/blob/main/sample_images/original_golden_bridge.jpg?raw=true",
            "image-two":"https://github.com/garret123h/image-comparison-api/blob/main/sample_images/old_photo.jpg?raw=true"
            }' 


Note: where the '-u admin' is, replace admin with your username.
Add desired images either by relative path, absolute path, or URL.

The program does not take into consideration images that are different sizes. So only input same sized images.

Sample testing images:
![alt text](https://github.com/garret123h/image-comparison-api/blob/main/run_program.png?raw=true)
![alt text](https://github.com/garret123h/image-comparison-api/blob/main/curl_one.png?raw=true)
![alt text](https://github.com/garret123h/image-comparison-api/blob/main/curl_two.png?raw=true)
