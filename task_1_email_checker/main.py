import dns.resolver
import smtplib
import socket
import sys
import os


def check_email(email):
    domain = email.split('@')[-1]

    # 1. Проверка MX-записей
    try:
        resolver = dns.resolver.Resolver()
        resolver.timeout = 5
        resolver.lifetime = 5
        mx_records = resolver.resolve(domain, 'MX')
        mx_host = str(mx_records[0].exchange).rstrip('.')
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        return "домен отсутствует"
    except Exception:
        return "MX-записи отсутствуют или некорректны"

    # 2. SMTP Handshake
    try:
        with smtplib.SMTP(host=mx_host, port=25, timeout=7) as server:
            server.helo(socket.gethostname())
            server.mail('test@example.com')
            code, _ = server.rcpt(email)

            if code == 250:
                return "домен валиден"
            else:
                return f"домен валиден, почтовый ящик не найден (код {code})"
    except Exception:
        # Если порт 25 закрыт, мы все равно подтвердили наличие домена и MX
        return "домен валиден (SMTP-проверка недоступна)"


if __name__ == "__main__":
    # Читаем путь к файлу из аргументов или используем дефолтный emails.txt
    file_path = sys.argv[1] if len(sys.argv) > 1 else 'emails.txt'

    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        sys.exit(1)

    with open(file_path, 'r') as f:
        emails = [line.strip() for line in f if line.strip()]

    for email in emails:
        print(f"{email}: {check_email(email)}")
