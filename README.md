

# linefollow
Simple script to follow a black line with 1 sensor attached

1.  Start clone the git to your Raspberry pi
      ```python
      git clone https://github.com/PhysX-82/linefollow.git
      ```

2. Then go to the folder

      ```pyhton
      cd linefollow
      ```

3. Then run the script, select wich script with the name of the file.

    Hard Track:
      ```python    
      python hardtrack.py
      ```
    Easy Track:
   
      ```python
      python easytrack.py
      ```

4. If the car cant finnish the tracks go adjust the parameters en either easytrack.py or hardtrack.py to your cars settings.

Errors

    ImportError: No module named yaml

    install the yaml module: apt-get install python-yaml

