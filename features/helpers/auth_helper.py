from features.pages.login_page import LoginPage

def login(context, email="anatestedesafio@gmail.com", password="senhaenjoeiteste"):
    """Realiza login e retorna a página inicial"""
    return (LoginPage(context.driver)
            .open()
            .enter_email(email)
            .enter_password(password)
            .submit())