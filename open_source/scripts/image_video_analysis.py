python
import cv2
import torch
from torchvision import models, transforms
from PIL import Image

# Load pre-trained model
model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Preprocess image
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.ToTensor(),
    ])
    image = Image.open(image_path)
    return transform(image).unsqueeze(0)

# Perform object detection
def detect_objects(image_tensor):
    with torch.no_grad():
        predictions = model(image_tensor)
    return predictions

# Process video
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        image_tensor = preprocess_image(frame)
        predictions = detect_objects(image_tensor)
        # Process predictions (e.g., draw bounding boxes on frame)
        for prediction in predictions:
            boxes = prediction['boxes'].cpu().numpy()
            for box in boxes:
                cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'path_to_your_image.jpg'
    image_tensor = preprocess_image(image_path)
    predictions = detect_objects(image_tensor)
    print(f"Predictions: {predictions}")

    video_path = 'path_to_your_video.mp4'
    process_video(video_path)
