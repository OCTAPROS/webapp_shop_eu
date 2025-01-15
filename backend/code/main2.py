from core.config import settings
from core.security import Hasher


print(Hasher.get_password_hash("admin123"))
