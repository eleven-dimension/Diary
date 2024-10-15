import re
import os


def remove_angle_brackets(s):
    if s[0] == "<" and s[-1] == ">":
        return s[1:-1]
    return s


def rename_images(root_path):
    md_file_path = f"{root_path}/main.md"
    with open(md_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    images_names = re.findall(r"!\[.*?\]\((.+)\)", content)
    new_image_name_dict = {}

    for image_name in images_names:
        if image_name not in new_image_name_dict:
            image_name_without_angle_brackets = remove_angle_brackets(image_name)

            image_extension = re.search(
                r"\.([a-zA-Z0-9]+)$", image_name_without_angle_brackets
            ).group(1)
            new_image_name_dict[image_name] = (
                f"image_{len(new_image_name_dict):02}.{image_extension}"
            )

    for old_name, new_name in new_image_name_dict.items():
        content = content.replace(old_name, new_name)
        old_name_without_angle_brackets = remove_angle_brackets(old_name)
        os.rename(
            f"{root_path}/{old_name_without_angle_brackets}", f"{root_path}/{new_name}"
        )

    with open(md_file_path, "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    for dirpath, dirnames, filenames in os.walk("./"):
        if "main.md" in filenames:
            rename_images(dirpath)
