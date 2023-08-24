import asyncio


async def get_audio(link: str) -> str:
    link = f"https://youtube.com{results[0]['url_suffix']}"
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "bestaudio",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    return (1, stdout.decode().split("\n")[0]) if stdout else (0, stderr.decode())
