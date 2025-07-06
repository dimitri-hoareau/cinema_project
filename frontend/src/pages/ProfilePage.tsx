import { useAuth } from "../context/AuthContext";

const ProfilePage = () => {
  const { user } = useAuth();

  if (!user) {
    return <p>Chargement du profil...</p>;
  }

  return (
    <div>
      <h2>Mon Profil</h2>
      <p>
        <strong>Nom d'utilisateur :</strong> {user.username}
      </p>
      <p>
        <strong>ID :</strong> {user.id}
      </p>
    </div>
  );
};

export default ProfilePage;
