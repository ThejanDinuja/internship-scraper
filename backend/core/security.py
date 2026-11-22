from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from core.config import AUTH0_DOMAIN, AUTH0_AUDIENCE
import jwt
from sqlmodel import Session, select
from db.session import get_session
from models.user import User

jwks_client = jwt.PyJWKClient(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
# print(jwks_client.uri)
bearer_scheme = HTTPBearer()

def verify_token(token: str) -> dict:
    try:
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        claims = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            audience=AUTH0_AUDIENCE,
            issuer=f"https://{AUTH0_DOMAIN}/"
        )
        return claims
    except jwt.PyJWTError:
        # print("Token error:", repr(e))
        raise HTTPException(status_code=401, detail="Invalid token or expired token")


def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
        session: Session = Depends(get_session),
) -> User:
    claims = verify_token(credentials.credentials)
    auth0_id = claims["sub"]

    user = session.exec(select(User).where(User.auth0id == auth0_id)).first()
    if user is None:
        user = User(auth0id=auth0_id)
        session.add(user)
        session.commit()
        session.refresh(user)

    return user
