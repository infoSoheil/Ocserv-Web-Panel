Ocserv(OpenConnect Server) And Ocserv User Management Pannel

    To instal this script run this command in your server :
    
        First clone project to your server :
            # git clone https://github.com/infoSoheil/Ocserv-Web-Panel.git && cd Ocserv-Web-Panel.git
    
        Then run this commands :
            # sudo chmod 755 install.sh
            # sudo bash install.sh


    login user pannel params : 

        # username : admin
        # password : admin
        

    use google reCAPTCHA for login page:

        # nano /var/www/html/ocserv_pannel/ocserv/settings.py 
        add your key instead of  'None' :
            GOOGLE_CAPTCHA_SITE_KEY = None
            GOOGLE_CAPTCHA_SECRET_KEY = None


    to sync db with ocpasswd file in pannel:
        
        # chmod 644 /etc/ocserv/ocpasswd 
    

    to deactive expire users add this line to crontab :
        
        # 1 0 * * *  /var/www/html/ocserv_pannel/venv/bin/python3 /var/www/html/ocserv_pannel/./manage.py deactive_account


    If there’s no web server running on your Ubuntu server and you want OpenConnect VPN server to use port 443, then you can use the standalone plugin to obtain TLS certificate from Let’s Encrypt. Run the following command. Don’t forget to set A record for your domain name.

        first install cert bot with this command :

        # sudo apt install certbot


        then make cerfiticate with this command

        # sudo certbot certonly --standalone --preferred-challenges http --agree-tos --email you@example.com -d vpn.example.com
        
            Dont forget edit this params :

            --email: you@example.com -> john.doe@gmail.com
            -d: vpn.example.com -> your domain or sub domain