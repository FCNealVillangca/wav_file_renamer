import os
import shutil

# Set the source and destination folders
src_folder = 'src'
dist_folder = 'dist'


if not os.path.exists(dist_folder):
    os.makedirs(dist_folder)

# Read the new filename prefix from a .txt file
with open('artist_name.txt', 'r') as f:
    new_file_name = f.read().strip()


# Get the list of .wav files in the source folder
wav_files = [f for f in os.listdir(src_folder) if f.endswith('.wav')]

# Get the current count of files in the destination folder
count = len([f for f in os.listdir(dist_folder) if f.endswith('.wav')])

# Rename and move the files
for file in wav_files:
    filename, file_extension = os.path.splitext(file)
    file_number = count+1
    new_name = f'{new_file_name}{count+1}{file_extension}'
    shutil.move(os.path.join(src_folder, file),
                os.path.join(dist_folder, new_name))
    count += 1

print(f'Moved {len(wav_files)} files to {dist_folder}')
