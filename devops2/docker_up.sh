#Starting the containers
docker run -d --name api-test-v2 -p 80:5000 --network devops mentorembeddeddevops/rest-api-test
docker run -d -e MYSQL_ROOT_PASSWORD=secret -p 3306:3306 --name mysql-test-v2 --network devops mentorembeddeddevops/mysql-test

echo ""

#Create volume which points to our directory
printf "Creating volume\n"
docker volume create --driver local --opt type=none --opt device=/mnt/c/Users/Gergő/Documents/GitHub/devops/devops2 --opt o=bind devopsvol

echo ""

#Build and run the python container, 
docker build -t python-test-v2 .
docker run -d --name python-test-v2 --network devops -v devopsvol:/app python-test-v2