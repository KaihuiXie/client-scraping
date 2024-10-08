from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from datetime import datetime


app = Flask(__name__)
from flask_cors import CORS
CORS(app)

# MySQL 配置信息
mysql_config = {
    'host': '127.0.0.1',
    'user': 'contact_user',
    'password': '1688Contacts',
    'database': 'contact_db'
}

# 连接到 MySQL 数据库
def get_db_connection():
    try:
        connection = mysql.connector.connect(**mysql_config)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# 保存联系人信息到数据库
@app.route('/saveContact', methods=['POST'])
def save_contact():
    contact = request.json
    connection = get_db_connection()
    if connection is None:
        return jsonify({"status": "error", "message": "Database connection failed"}), 500

    cursor = connection.cursor()
    try:

        # 检查联系人是否已存在
        cursor.execute("SELECT * FROM contacts WHERE memberId = %s", (contact['memberId'],))
        result = cursor.fetchone()

        if result:
            print('Contact exists: ', contact.get('memberId', ''), '/', contact.get('companyName', ''))
            return jsonify({"status": "exists", "message": "Contact already exists"}), 200
        #print(contact.get('name', 'none'))
        # 插入数据
        query = """
        INSERT INTO contacts (name, mobileNo, phoneNum, address, companyName, jobTitle, domain, isMale, moreInfoLink, memberId, qrCode, pageUrl, crawl_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Get current time
        crawl_time = datetime.now()

        cursor.execute(query, (
            contact.get('name', ''),
            contact.get('mobileNo', ''),
            contact.get('phoneNum', ''),
            contact.get('address', ''),
            contact.get('companyName', ''),
            contact.get('jobTitle', ''),
            contact.get('domain', ''),
            contact.get('isMale', ''),
            contact.get('moreInfoLink', ''),
            contact.get('memberId', ''),
            contact.get('qrCode', ''),
            contact.get('pageUrl', ''),
            crawl_time  # Insert crawl time
        ))
        connection.commit()
        print('success: ', contact.get('memberId', ''), '/', contact.get('companyName', ''))
        return jsonify({"status": "success", "message": "Contact saved"}), 201
    except Error as e:
        print(f"Error inserting contact: {e}")
        return jsonify({"status": "error", "message": "Failed to save contact"}), 500
    finally:
        cursor.close()
        connection.close()

# 获取所有联系人信息
@app.route('/getContacts', methods=['GET'])
def get_contacts():
    connection = get_db_connection()
    if connection is None:
        return jsonify({"status": "error", "message": "Database connection failed"}), 500

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        return jsonify(contacts), 200
    except Error as e:
        print(f"Error retrieving contacts: {e}")
        return jsonify({"status": "error", "message": "Error retrieving contacts"}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
