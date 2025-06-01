import boto3
from botocore.client import Config

# Cấu hình truy cập MinIO đúng IP và port
s3 = boto3.client('s3',
    endpoint_url='http://172.20.10.4:9000',
    aws_access_key_id='LuuGiaPhong',         # Thay bằng Access Key bạn đã tạo trong MinIO
    aws_secret_access_key='12345678',      # Thay bằng Password bạn đã đặt
    config=Config(signature_version='s3v4'),
    region_name='us-east-1')

# Liệt kê file trong bucket để chắc chắn file tồn tại
response = s3.list_objects_v2(Bucket='iot-lab-demo')
if 'Contents' not in response:
    print("Bucket không có file hoặc bạn không có quyền truy cập.")
else:
    print("Danh sách file:")
    for obj in response['Contents']:
        print("-", obj['Key'])

    # Thử tải file nếu tìm thấy
    try:
        s3.download_file('iot-lab-demo', 'sensor_data.csv', 'temp.csv')
        print("Download thành công!")
    except Exception as e:
        print("Lỗi khi tải file:", e)
