#!/bin/sh

echo $1 
echo $2

echo -n | openssl s_client -connect $1:$2 -tls1_1  2>&1 | grep -e Cipher -e Protocol
echo -n | openssl s_client -connect $1:$2 -tls1_2  2>&1 | grep -e Cipher -e Protocol
echo -n | openssl s_client -connect $1:$2 -tls1  2>&1 | grep -e Cipher -e Protocol
echo -n | openssl s_client -connect $1:$2 -ssl3  2>&1 | grep -e Cipher -e Protocol
echo -n | openssl s_client -connect $1:$2 -ssl2  2>&1 | grep -e Cipher -e Protocol


