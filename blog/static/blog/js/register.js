function validate_required(field,alerttxt)
{
    with (field)
    {
        if (value==null||value=="")
        {
            alert(alerttxt);return false;
        }
        else 
        {
            return true
        }
    }
}

function validate_form(thisform)
{
    with (thisform)
    {
        if (validate_required(account,"请填写账号!")==false)
        {
            account.focus();return false
        }
        else if (validate_required(password,"请填写密码!")==false)
        {
            password.focus();return false
        }
        else if (validate_required(password_second,"请再次输入密码!")==false)
        {
            password_second.focus();return false
        }
        else if (validate_required(nickname,"请填写昵称!")==false)
        {
            nickname.focus();return false
        }
        else if (validate_required(email,"请填写邮件地址!")==false)
        {
            email.focus();return false
        }
        else if (validate_required(age,"请填写年龄!")==false)
        {
            age.focus();return false
        }
        else if (validate_required(address,"请填写地址!")==false)
        {
            address.focus();return false
        }
    }
}