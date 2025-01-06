# Microsoft Paint Test Cases Summary

| No. | ID | Test Purpose | Instructions | Test Method | Evaluation Method | Source |
|-----|----|--------------|--------------|--------------|--------------------|---------|
| 1 | 15f8de6e-3d39-40e4-af17-bdbb2393c0d9-WOS | Verify basic drawing functionality | Open Paint and draw a red circle | 1. Wait for 2 seconds<br>2. Draw a red circle | 1. Activate "Untitled - Paint" window<br>2. Take screenshot<br>3. Save as Screenshot.png<br>4. Check if red circle is present in the image<br>5. Close Paint | Microsoft Corporation |
| 2 | 3544ac9a-6aee-4a0b-a203-bc7b59b272b6-WOS | Verify file saving functionality | Save the Paint image as "circle.png" in the downloads folder | 1. Open Paint<br>2. Wait for 1 second<br>3. Save file | Check if file "circle.png" exists in<br>C:\Users\Docker\Downloads | Microsoft Corporation |
| 3 | 44dbac63-32bf-4cd2-81b4-ad6803ec812d-WOS | Verify canvas size modification | Change the canvas size to 800x600 pixels | 1. Open Paint<br>2. Wait for 1 second<br>3. Change canvas size | 1. Activate "Untitled - Paint" window<br>2. Save image<br>3. Verify image dimensions are 800x600<br>4. Close Paint | Microsoft Corporation | 