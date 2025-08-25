# from fastapi import FastAPI, File, UploadFile, HTTPException
# from fastapi.responses import StreamingResponse
# from PIL import Image
# from pathlib import Path
# import io
# import zipfile
# import tempfile
# import shutil
# import os
#
# app = FastAPI(title="WebP to JPEG Converter API", description="Конвертация WebP в JPEG")
#
# @app.post("/convert-webp/", response_class=StreamingResponse)
# async def convert_webp_files(files: list[UploadFile] = File(...)):
#     with tempfile.TemporaryDirectory() as output_dir:
#         output_path = Path(output_dir)
#         converted_files = []
#
#         for file in files:
#             if not file.filename.lower().endswith(".webp"):
#                 raise HTTPException(status_code=400, detail=f"Файл {file.filename} не WebP")
#             try:
#                 content = await file.read()
#                 img = Image.open(io.BytesIO(content)).convert("RGB")
#                 output_file = output_path / f"{Path(file.filename).stem}.jpg"
#                 output_file.parent.mkdir(parents=True, exist_ok=True)
#                 img.save(output_file, "JPEG", quality=95)
#                 converted_files.append(output_file)
#             except Exception as e:
#                 print(f"Ошибка конвертации {file.filename}: {str(e)}")
#
#         if not converted_files:
#             raise HTTPException(status_code=400, detail="Нет валидных WebP файлов")
#
#         output_zip = output_path / "converted_images.zip"
#         with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zip_ref:
#             for jpeg_file in converted_files:
#                 zip_ref.write(jpeg_file, jpeg_file.relative_to(output_path))
#
#         with open(output_zip, "rb") as f:
#             content = f.read()
#
#         return StreamingResponse(
#             io.BytesIO(content),
#             media_type="application/zip",
#             headers={"Content-Disposition": "attachment; filename=converted_images.zip"}
#         )
#
# @app.post("/convert-zip/", response_class=StreamingResponse)
# async def convert_webp_zip(file: UploadFile = File(...)):
#     if not file.filename.lower().endswith(".zip"):
#         raise HTTPException(status_code=400, detail="Загрузите .zip файл")
#
#     with tempfile.TemporaryDirectory() as input_dir, tempfile.TemporaryDirectory() as output_dir:
#         input_path = Path(input_dir)
#         output_path = Path(output_dir)
#         zip_path = input_path / file.filename
#
#         with open(zip_path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)
#
#         with zipfile.ZipFile(zip_path, "r") as zip_ref:
#             zip_ref.extractall(input_path)
#
#         converted_files = []
#         for webp_file in input_path.rglob("*.webp"):
#             try:
#                 with Image.open(webp_file) as img:
#                     rgb_img = img.convert("RGB")
#                     output_file = output_path / f"{webp_file.stem}.jpg"
#                     output_file.parent.mkdir(parents=True, exist_ok=True)
#                     rgb_img.save(output_file, "JPEG", quality=95)
#                     converted_files.append(output_file)
#             except Exception as e:
#                 print(f"Ошибка конвертации {webp_file.name}: {str(e)}")
#
#         if not converted_files:
#             raise HTTPException(status_code=400, detail="Нет валидных WebP файлов в архиве")
#
#         output_zip = output_path / "converted_images.zip"
#         with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zip_ref:
#             for jpeg_file in converted_files:
#                 zip_ref.write(jpeg_file, jpeg_file.relative_to(output_path))
#
#         with open(output_zip, "rb") as f:
#             content = f.read()
#
#         return StreamingResponse(
#             io.BytesIO(content),
#             media_type="application/zip",
#             headers={"Content-Disposition": "attachment; filename=converted_images.zip"}
#         )
#
# @app.get("/")
# async def root():
#     return {"message 1": "API для конвертации WebP в JPEG. Используйте /docs для Swagger UI."}