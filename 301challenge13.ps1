#Script:                       Ops 301 Ops Chall 13
# Author:                       carlos rojas 
# Date of latest revision:      06/14/2023
# Purpose:                       Powershell AD Automation

# Set the user details
$firstName = "Franz"
$lastName = "Ferdinand"
$displayName = "$firstName $lastName"
$officeLocation = "Springfield, OR"
$department = "TPS Department"
$email = "ferdi@GlobeXpower.com"

# Create the new user in Active Directory
New-ADUser -SamAccountName $firstName.ToLower() -GivenName $firstName -Surname $lastName -Name $displayName `
    -DisplayName $displayName -UserPrincipalName "$firstName.$lastName@admin.globex.com" `
    -Enabled $true -Office $officeLocation -Department $department -EmailAddress $email
