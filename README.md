# Image comparison API

## Instructions
Open terminal and navigate to directory.<br />
Type in 'python3 app.py && uvicorn app:app --reload' <br /> 
Now enter into a new tab and enter some curl commands such as; <br />
curl http://127.0.0.1:8000/compare/kmrhn74zgzcq4nqb \
  --header "Content-Type: application/json" \
  --request GET\
  --data '{"image_one":"./sample_images/original_golden_bridge.jpg",
            "image_two":"./sample_images/old_photo.jpg"
            }' 

or 

curl http://127.0.0.1:8000/compare/kmrhn74zgzcq4nqb \
  --header "Content-Type: application/json" \
  --request GET\
  --data '{"image_one":"https://github.com/garret123h/image-comparison-api/blob/main/sample_images/original_golden_bridge.jpg?raw=true",
            "image_two":"https://github.com/garret123h/image-comparison-api/blob/main/sample_images/old_photo.jpg?raw=true"
            }' 

Sample testing images:<br />
![alt text](https://github.com/garret123h/image-comparison-api/blob/main/run_program.png?raw=true)
![alt text](https://github.com/garret123h/image-comparison-api/blob/main/curl_one.png?raw=true)
![alt text](https://github.com/garret123h/image-comparison-api/blob/main/curl_two.png?raw=true)
