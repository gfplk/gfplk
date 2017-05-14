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
		else if (validate_required(check_code,"请填写验证码!")==false)
		{
			check_code.focus();return false
		}
	}
}