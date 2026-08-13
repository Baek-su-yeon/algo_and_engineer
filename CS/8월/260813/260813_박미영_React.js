// 1. 기존 JavaScript의 화면 변경 방식
// JavaScript에서는 데이터가 변경되면 개발자가 DOM 요소를 직접 찾아 수정

let likeCount = 0;

button.addEventListener("click", () => {
  likeCount += 1;

  document.querySelector("#like-count").textContent = likeCount;
});

// 2. React의 화면 변경 방식
// React에서는 DOM을 직접 변경하는 대신, 현재 데이터에 따라 화면이 어떻게 보여야 하는지 작성
<button>좋아요 {likeCount}</button>

// 3. 좋아요 버튼을 하나의 컴포넌트로 구성
function LikeButton() {
  return <button>좋아요</button>;
}

// 게시글도 별도의 컴포넌트로 구성
function PostCard() {
  return (
    <article>
      <h2>미영</h2>
      <p>React를 공부했습니다.</p>
      <LikeButton />
    </article>
  );
}

// 4. JSX
<h1>Hello</h1>


// JSX는 HTML처럼 보이지만 실제로는 빌드 과정에서 JavaScript로 변환됨.
React.createElement("h1", null, "Hello");

// 5. Props
function App() {            // 부모 컴포넌트
  return (
    <>
      <PostCard
        username="미영"
        content="React를 공부했습니다."
      />

      <PostCard
        username="민수"
        content="데이터베이스를 공부했습니다."
      />
    </>
  );
}

// PostCard 컴포넌트는 username과 content라는 props를 받아 화면에 표시
function PostCard({ username, content }) {  // 자식 컴포넌트 
  return (
    <article>
      <h2>{username}</h2>
      <p>{content}</p>
    </article>
  );
}

// 6. State
function LikeButton() { // <- 함수 컴포넌트 : 함수 형태로 만든 React 컴포넌트
  const [likeCount, setLikeCount] = useState(0);
  // 0은 likeCount에만 들어가고, setLikeCount는 상태변경함수, 0이 할당되는 건 아님.

  return (
    <button onClick={() => setLikeCount(likeCount + 1)}>
      좋아요 {likeCount}
    </button>
  );
}

// 7. 단방향 데이터 흐름
// 부모는 State와 함께 State를 변경할 수 있는 함수를 자식에게 전달
function App() {
  const [likeCount, setLikeCount] = useState(0);

  return (
    <PostCard
      likeCount={likeCount}
      onLike={() => setLikeCount(likeCount + 1)} 
    />
  );
}

// 자식은 전달받은 함수를 버튼에 연결
function PostCard({ likeCount, onLike }) {
  return (
    <button onClick={onLike}>
      좋아요 {likeCount}
    </button>
  );
}

// 8. 리렌더링
//이전 Virtual DOM : <button>좋아요 0</button>
//새 Virtual DOM : <button>좋아요 1</button>

// 9. React.memo
const Profile = React.memo(function Profile({ username }) {
  return <h2>{username}</h2>;
});
