## Week 2 Notes

1. How are drones used for aerial imagery purposes?  
   1. Uses:  
      1. Search and rescue  
      2. Law enforcement  
      3. Agriculture  
      4. Environment stuff  
      5. Competitions  
   2. Uses many types of aerial imagery:  
      1. Oblique vs nadir  
      2. RGB-D vs plain RGB vs multi-spectral

2. How is OpenCV used for computer vision purposes? How do we use it as a club?  
   1. General-purpose CV library  
   2. Free & open source  
   3. General-purpose uses:  
      1. Feature detection  
      2. 3D reconstruction  
      3. Motion analysis  
      4. Optical flow  
      5. Photo manipulation / de-blurring  
      6. Video editing / reading / writing  
   4. Club uses:  
      1. Feature detection (SIFT, Feature Matching)  
      2. Feature matching  
      3. Image manipulation  
3. What are some pre-made alternatives to writing our own aerial imagery code, and how do they work? What are the drawbacks?  
   1. OpenDroneMap  
   2. How it works:  
      1. Get pictures with Geo tags  
      2. Adjust \~50 settings (from trial and error there’s a good group of settings found)  
      3. Wait for ODM to do its stuff  
   3. Benefits:  
      1. Simple to use  
      2. Nice APIs  
      3. Interesting API (like entire 3D model)  
   4. Drawbacks:  
      1. Not optimized for in-flight use  
      2. Slow unless carefully optimized with settings  
      3. Requires accurate GPS tags  
      4. Too feature-rich for all we want  
         1. All we want is an orthophoto\!  
4. What’s the next steps forward as a club?  
   1. Create a custom OpenCV algorithm to do our own stitching real-time on the drone OR tweak ODM settings to work real-time automatically  
   2. SLAM  
   3. Optical Flow  
   4. Structure from Motion  
   5. Applying drone imagery

