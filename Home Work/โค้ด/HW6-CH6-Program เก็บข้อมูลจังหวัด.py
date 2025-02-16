#นายก้องภพ บำรุงแจ้ง
#นายญาณพัฒน์ ต่วนป้องค่าย
#นายพสุธร ปรุงเกียรติ

def insert_data(region_data):
    region = input("ป้อนชื่อภูมิภาค: ")
    province = input("ป้อนชื่อจังหวัด: ")
    if region not in region_data:
        region_data[region] = []
    region_data[region].append(province)
    print(f"จังหวัด '{province}' ถูกเพิ่มไปยังภาค '{region}'.")


def update_data(region_data):
    region = input("ป้อนชื่อภาคของจังหวัดที่ต้องการแก้ไข: ")
    old_province = input("ป้อนชื่อจังหวัดที่ต้องการแก้ไข: ")
    
    if region in region_data and old_province in region_data[region]:
        new_province = input("ป้อนชื่อจังหวัดใหม่: ")
        index = region_data[region].index(old_province)
        region_data[region][index] = new_province
        print(f"แก้ไขชื่อจังหวัด {old_province} เป็น {new_province} สำเร็จ!")
    else:
        print("ไม่พบจังหวัดที่ต้องการแก้ไข")

def search_data(region_data):
    province = input("ค้นหาจังหวัดจากชื่อ: ")
    found = False

    for region, provinces in region_data.items():
        if province in provinces:
            print(f"จังหวัด {province} ภาค {region}")
            found = True
            break
    
    if not found:
        print("ไม่พบข้อมูล")

def delete_data(region_data):
    region = input("ป้อนชื่อภาคของจังหวัดที่ต้องการลบ: ")
    province = input("ป้อนชื่อจังหวัดที่ต้องการลบ: ")
    
    if region in region_data and province in region_data[region]:
        region_data[region].remove(province)
        print(f"ลบจังหวัด {province} ออกจาก {region} สำเร็จ!")
    else:
        print("ไม่พบจังหวัดที่ต้องการลบ")


def view_all_data(region_data):
    for region, provinces in region_data.items():
        print(f"{region}: {', '.join(provinces)}")


def main():
    province_data = {}
    while True:
        print("\nMenu:")
        print("1. Insert Data")
        print("2. Update Data")
        print("3. Search Data")
        print("4. Delete Data")
        print("5. View All Data")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            insert_data(province_data)
        elif choice == '2':
            update_data(province_data)
        elif choice == '3':
            search_data(province_data)
        elif choice == '4':
            delete_data(province_data)
        elif choice == '5':
            view_all_data(province_data)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()