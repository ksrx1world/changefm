make a new virtualenv if needed 
then 
you need to run this command

    pip install --editable .

 
afterwards 
run command in the shell to change your Ip address

    changefn ip enp0s3  



where "changefn" is your script name ,"ip" is the function within script, "enp0s3" is your adapter name
If you don't enter adapter name then bydefault it will take "enp0s3" as a adapter.

same for changing subnet

    changefn subnet enp0s3



same for changing gateway 

    changefn gateway enp0s3    