make a new virtualenv if needed 
then 
you need to run this command

    pip install --editable .

 
afterwards 
run command in the shell to change your Ip address

    changeip enp0s3  



where changeip is a function which changes ip within changefn module, "enp0s3" is your adapter name
If you don't enter adapter name then bydefault it will take "enp0s3" as a adapter.

same for changing subnet

    changesubnet enp0s3


same for changing gateway 

    changegateway enp0s3    