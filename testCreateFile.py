import os
import uuid
import shutil
import yaml
from repository.SampleRepository import SampleRepository
from model.Sample import Sample


def createFile(samples):
    # Đường dẫn đến thư mục chính của bạn (thay đổi nếu cần)
    project_directory = "D:\\test flask cors"

    # Tạo tên ngẫu nhiên
    random_name = str(uuid.uuid4())

    # Tạo thư mục 'data' nếu nó chưa tồn tại
    data_directory = os.path.join(project_directory, random_name)
    os.makedirs(data_directory, exist_ok=True)

    # Tạo thư mục 'images' và 'labels' bên trong thư mục 'data'
    images_directory = os.path.join(data_directory, "images")
    labels_directory = os.path.join(data_directory, "labels")
    os.makedirs(images_directory, exist_ok=True)
    os.makedirs(labels_directory, exist_ok=True)

    # Tạo thư mục 'train' bên trong thư mục 'images' và 'labels'
    train_images_directory = os.path.join(images_directory, "train")
    train_labels_directory = os.path.join(labels_directory, "train")
    os.makedirs(train_images_directory, exist_ok=True)
    os.makedirs(train_labels_directory, exist_ok=True)

    for sample in samples:
        sample = Sample(sample)
        path = sample.path
        source_image_path = path
        label_path = path.replace("images", "labels")
        label_path = label_path.replace("png", "txt")

        # Đường dẫn mới cho tệp hình ảnh trong thư mục 'train'
        new_image_path = os.path.join(train_images_directory, os.path.basename(source_image_path))

        # Sao chép tệp hình ảnh vào thư mục 'train'
        shutil.copyfile(source_image_path, new_image_path)

        new_label_path = os.path.join(train_labels_directory, os.path.basename(label_path))

        # Sao chép tệp hình ảnh vào thư mục 'train'
        shutil.copyfile(label_path, new_label_path)

    # Tạo nội dung cho tệp YAML
    yaml_content = {
        "path": os.path.join("D:\\test flask cors", random_name),
        "train": "images\\train",
        "val": "images\\train",
        "names": {
            0: "traffic_sign"
        }
    }

    # Tạo và ghi nội dung vào tệp YAML
    config_file_path = os.path.join(data_directory, "config.yaml")
    with open(config_file_path, "w") as config_file:
        yaml.dump(yaml_content, config_file, default_flow_style=False)

    # In ra đường dẫn của tệp YAML
    print(f"Đường dẫn tới tệp YAML: {config_file_path}")

    return data_directory

def deleteFile(name):
    directory_to_delete = name

    # Xóa thư mục và nội dung bên trong
    shutil.rmtree(directory_to_delete)

# file_name = createFile("D:\\test flask cors\\data1\\images\\train\\00.png")
#
#
# deleteFile(file_name)

# list_Id = (42, 43, 45)
#
# samples = []
#
# for id in list_Id:
#     samples.append(SampleRepository.getSampleById(id))
# filename = createFile(samples)


