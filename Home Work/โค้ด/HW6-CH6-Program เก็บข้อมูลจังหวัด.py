#นายก้องภพ บำรุงแจ้ง
#นายญาณพัฒน์ ต่วนป้องค่าย
#นายพสุธร ปรุงเกียรติ

def insert_data(region_data):
    region = input("Enter region(North, Central, Northeast, South): ")
    province = input("Enter province name: ")
    if region not in region_data:
        region_data[region] = []
    region_data[region].append(province)
    print(f"Province '{province}' Added to '{region}'.")

def update_data(region_data):
    region = input("Enter Region of the province you want to change: ")
    old_province = input("Enter province that you want to change: ")
    
    if region in region_data and old_province in region_data[region]:
        new_province = input("Enter new province name: ")
        index = region_data[region].index(old_province)
        region_data[region][index] = new_province
        print(f"Change  {old_province} to {new_province} success!")
    else:
        print("Province not found")

def search_data(region_data):
    province = input("Search province by name: ")
    found = False

    for region, provinces in region_data.items():
        if province in provinces:
            print(f"Province {province} region {region}")
            found = True
            break
    
    if not found:
        print("Province not found")

def delete_data(region_data):
    region = input("Enter region of the province name you want to delete: ")
    province = input("Enter province name you want to delete: ")
    
    if region in region_data and province in region_data[region]:
        region_data[region].remove(province)
        print(f"Delete {province} from {region} success!")
    else:
        print("Province not found")


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