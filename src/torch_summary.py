import model as models
import torch


from torchinfo import summary

model = models.model()
print(model)

summary(model, input_size=(1, 3, 256, 128))

# from torchsummary import summary
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# model = models.convnexts_tiny().to(device)
# summary(model, (3, 256, 128))
