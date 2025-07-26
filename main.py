import json
from pathlib import Path
from yt_dlp import YoutubeDL


def get_json():
    course_json = input("Nome do seu json: ")
    with open(f"{course_json}.json", "r") as file:
        course_data = json.load(file)
    return course_data


def main():
    course_data = get_json()["course"]
    course_name = course_data["name"]

    course_modules = course_data["modules"]
    for module in course_modules:
        module_order = module["order"]
        module_name = f"{module_order:03d} - {module['name']}"

        module_lessons = module["lessons"]
        for lesson in module_lessons:
            lesson_order = lesson["order"]
            lesson_title = f"{lesson_order:03d} - {lesson['title']}"
            files = lesson["files"]

            if files:
                pass

            video = lesson.get("video", "")
            if video:
                mp4_url = video["download_link_full_url"]

                path = Path(f"{course_name}/{module_name}/{lesson_title}")
                path.mkdir(parents=True, exist_ok=True)

                ydl_opts = {
                    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
                    "outtmpl": str(path / "video.%(ext)s"),
                    "noplaylist": True,
                    "quiet": True,
                }

                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([mp4_url])


if __name__ == "__main__":
    main()
