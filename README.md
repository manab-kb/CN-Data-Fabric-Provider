# CN-Data-Fabric-Provider
A repository containing an implementation of a blockchain based decentralized and distributed data fabric provider for intermittent communication, targeted towards improving unmanned vehicular communication (UAV's).

# How to run ?
1. Clone the **main** branch of this repository to your local machine.
2. Make changes to the path present in the following lines within the following files (to match the directory within your local machine where the repository is cloned):

        a. Line 16 and 21 : Blockchain/blockchain.py
    
        b. Line 14 - GCS/gcs.py
     
        c. Line 30 - Network/server.py

        d. Line 82 - UAV/uav.py
3. `pip install -r requirements.txt`  - to install all the requirements present within the requirements.txt file.
4. Depending on the OS on which the program is being run; run the following commands within the cloned repository:

    a. `python .\Runner-GCS.py` / `python3 Runner-GCS.py`

    b. `python .\Runner-UAV.py` / `python3 Runner-UAV.py`

# Contributing to CN-Data-Fabric-Provider
Hello and welcome! We are so glad that you are interested in contributing to CN Data Fabric Provider!
We only have a couple of rules and we hope you enjoy the process :)

## Contributing Rules
1. Don't move or delete any files. Only modify them.

## Contributing Process
1. Fork the repository
2. Clone your forked repository to your computer
3. Head to the issues tab and look for an issue that you like.
4. Once you have decided what issue to work on, give it a shot!
5. Once done, push the code to your forked repository.
6. Head to the Pull Requests tab and click on "Create New Pull Request"
7. On the left of the arrow should be this repo and on the right should be yours.
8. Add a small description to the Pull Request describing what you've done.
9. Mention what Issue you have worked on. If the issue number is #3, you can mention "Closes #3" in the Pull Request description.
10. Submit Pull Request

It's that easy! We hope you enjoy contributing to our repository. Don't hesitate to contact any of the maintainers about any problems!
