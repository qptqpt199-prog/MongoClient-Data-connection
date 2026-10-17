from pymongo import MongoClient


def get_data():
  try:
    # Kết nối đến MongoDB (thay đổi URI nếu dùng MongoDB Atlas)
    client = MongoClient("mongodb://localhost:27017/")
    db = client["ten_database"]
    collection = db["ten_collection"]

    # Truy vấn dữ liệu (ví dụ lấy toàn bộ tài liệu trong collection)
    documents = collection.find()

    for doc in documents:
      print(doc)

  except Exception as e:
    print(f"Lỗi kết nối hoặc truy vấn: {e}")


if __name__ == "__main__":
  get_data()
