#!/bin/bash

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}Iniciando implantação do sistema Bancos...${NC}"

# Criar diretório do projeto
echo -e "${GREEN}Criando diretório do projeto...${NC}"
sudo mkdir -p /var/www/vestuar/bancos
cd /var/www/vestuar/bancos

# Clonar o repositório
echo -e "${GREEN}Clonando o repositório...${NC}"
sudo git clone https://github.com/rogaciano/bancos .

# Configurar permissões
echo -e "${GREEN}Configurando permissões...${NC}"
sudo chown -R www-data:www-data /var/www/vestuar/bancos

# Criar e ativar ambiente virtual
echo -e "${GREEN}Configurando ambiente virtual...${NC}"
sudo -u www-data python3 -m venv venv
source venv/bin/activate

# Instalar dependências
echo -e "${GREEN}Instalando dependências...${NC}"
sudo -u www-data venv/bin/pip install -r requirements.txt

# Coletar arquivos estáticos
echo -e "${GREEN}Coletando arquivos estáticos...${NC}"
sudo -u www-data venv/bin/python manage.py collectstatic --noinput

# Criar diretórios de log para o Gunicorn
echo -e "${GREEN}Configurando diretórios de log...${NC}"
sudo mkdir -p /var/log/gunicorn
sudo chown -R www-data:www-data /var/log/gunicorn

# Copiar e configurar arquivo de serviço do systemd
echo -e "${GREEN}Configurando serviço do systemd...${NC}"
sudo cp vestuar_bancos.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable vestuar_bancos
sudo systemctl start vestuar_bancos

# Configurar Nginx
echo -e "${GREEN}Configurando Nginx...${NC}"
# Substituir o caminho correto nos arquivos de configuração
sudo sed -i "s|/path/to/your/project|/var/www/vestuar/bancos|g" nginx_bancos.conf

# Copiar configuração do Nginx
sudo cp nginx_bancos.conf /etc/nginx/sites-available/vestuar_bancos
sudo ln -sf /etc/nginx/sites-available/vestuar_bancos /etc/nginx/sites-enabled/

# Testar configuração do Nginx
echo -e "${GREEN}Testando configuração do Nginx...${NC}"
sudo nginx -t

if [ $? -eq 0 ]; then
    # Reiniciar Nginx
    echo -e "${GREEN}Reiniciando Nginx...${NC}"
    sudo systemctl restart nginx
    echo -e "${GREEN}Implantação concluída com sucesso!${NC}"
    echo -e "${GREEN}O sistema está disponível em: http://144.202.29.245/vestuar/bancos${NC}"
else
    echo -e "${RED}Erro na configuração do Nginx. Por favor, verifique os logs.${NC}"
    exit 1
fi

# Verificar status dos serviços
echo -e "${GREEN}Status dos serviços:${NC}"
echo -e "\nStatus do Gunicorn:"
sudo systemctl status vestuar_bancos
echo -e "\nStatus do Nginx:"
sudo systemctl status nginx
